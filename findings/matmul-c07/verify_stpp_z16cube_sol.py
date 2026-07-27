#!/usr/bin/env python3
"""
Exact Sol-lineage verifier for a concrete simultaneous triple product
property (STPP) construction in H = (Z/16Z)^3.

Source of the construction:
  Cohn--Kleinberg--Szegedy--Umans (FOCS 2005), Definition 5.1 and
  Proposition 5.2, https://arxiv.org/abs/math/0511460

This script independently checks the construction from the definitions.  It
uses integer/modular arithmetic only.  Decimal logarithms are display-only;
every load-bearing comparison is also checked by an integer inequality.

For m = 16, let E_r be the nonzero part of coordinate axis r in (Z/mZ)^3:

  (A_0,B_0,C_0) = (E_0,E_1,E_2),
  (A_1,B_1,C_1) = (E_1,E_2,E_0).

The additive STPP condition used below is CKSU Definition 5.1:

  a_i-a'_j + b_j-b'_k + c_k-c'_i = 0  ==>  i=j=k,

and, on the diagonal i=j=k, the ordinary TPP forces the paired elements
to be equal.

The verifier has two independent checks:

  1. Count all six-variable STPP relations exactly by convolving difference
     multiplicities.  The six off-diagonal index patterns must have count 0;
     each of the two diagonal patterns must have exactly 15^3 relations,
     namely the intended equal-pair relations.

  2. Audit the concrete group-algebra embedding.  It checks that the 450
     left-variable locations, 450 right-variable locations, and 450 output
     locations are each collision-free, then enumerates all 450^2 products.
     Exactly 2*15^3 = 6750 products may hit an output location, and every one
     must be an intended matrix-multiplication monomial.
"""

from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product


MODULUS = 16
ZERO = (0, 0, 0)


def add(x, y):
    return tuple((a + b) % MODULUS for a, b in zip(x, y))


def sub(x, y):
    return tuple((a - b) % MODULUS for a, b in zip(x, y))


def neg(x):
    return tuple((-a) % MODULUS for a in x)


def axis(nonzero_coordinate):
    result = []
    for value in range(1, MODULUS):
        element = [0, 0, 0]
        element[nonzero_coordinate] = value
        result.append(tuple(element))
    return tuple(result)


E0, E1, E2 = (axis(coordinate) for coordinate in range(3))
TRIPLES = (
    (E0, E1, E2),
    (E1, E2, E0),
)


def difference_counter(left, right):
    """Multiplicity counter for {x-y : x in left, y in right}."""
    return Counter(sub(x, y) for x in left for y in right)


def stpp_relation_count(i, j, k):
    """
    Count the six-tuples satisfying

      a_i-a'_j + b_j-b'_k + c_k-c'_i = 0.

    Difference counters count all six-tuples, including multiplicities, while
    reducing the work from 15^6 direct iterations to a small exact convolution.
    """
    ai, _, ci = TRIPLES[i]
    aj, bj, _ = TRIPLES[j]
    _, bk, ck = TRIPLES[k]

    a_differences = difference_counter(ai, aj)
    b_differences = difference_counter(bj, bk)
    c_differences = difference_counter(ck, ci)

    count = 0
    for da, multiplicity_a in a_differences.items():
        for db, multiplicity_b in b_differences.items():
            needed_dc = neg(add(da, db))
            count += (
                multiplicity_a
                * multiplicity_b
                * c_differences.get(needed_dc, 0)
            )
    return count


def support_map(kind):
    """
    Construct a variable-to-group-location map for the simultaneous embedding.

      left  X_i[a,b] -> -a+b,
      right Y_i[b,c] -> -b+c,
      output Z_i[a,c] is read from -a+c.

    Returns group_location -> full variable label and rejects any collision.
    """
    supports = {}
    for block, (a_set, b_set, c_set) in enumerate(TRIPLES):
        if kind == "left":
            first, second = a_set, b_set
        elif kind == "right":
            first, second = b_set, c_set
        elif kind == "output":
            first, second = a_set, c_set
        else:
            raise ValueError(f"unknown support kind: {kind}")

        for first_element in first:
            for second_element in second:
                location = sub(second_element, first_element)
                label = (block, first_element, second_element)
                if location in supports:
                    raise AssertionError(
                        f"{kind} support collision at {location}: "
                        f"{supports[location]} versus {label}"
                    )
                supports[location] = label
    return supports


def audit_group_algebra_embedding():
    """
    Enumerate every product of an encoded left and right matrix variable.

    If such a product lands at any read-out coordinate, it must be exactly an
    intended monomial X_i[a,b]Y_i[b,c] contributing to Z_i[a,c].
    """
    left = support_map("left")
    right = support_map("right")
    output = support_map("output")

    output_hits = 0
    forbidden_aliases = []

    for left_location, left_label in left.items():
        for right_location, right_label in right.items():
            product_location = add(left_location, right_location)
            if product_location not in output:
                continue

            output_hits += 1
            output_label = output[product_location]
            left_block, a_element, b_element = left_label
            right_block, b_prime_element, c_element = right_label
            output_block, a_prime_element, c_prime_element = output_label

            intended = (
                left_block == right_block == output_block
                and a_element == a_prime_element
                and b_element == b_prime_element
                and c_element == c_prime_element
            )
            if not intended:
                forbidden_aliases.append(
                    (left_label, right_label, output_label)
                )

    return {
        "left_support": len(left),
        "right_support": len(right),
        "output_support": len(output),
        "tested_products": len(left) * len(right),
        "output_hits": output_hits,
        "forbidden_aliases": forbidden_aliases,
    }


def full_axis(coordinate):
    result = []
    for value in range(MODULUS):
        element = [0, 0, 0]
        element[coordinate] = value
        result.append(tuple(element))
    return tuple(result)


def verify_single_tpp_tight_witness():
    """
    Verify the ordinary abelian TPP cap is attained by the three full axes.

    The sum map is a bijection from F0 x F1 x F2 to H, so this realizes one
    <16,16,16> tensor.  Conversely, injectivity of the sum map for every
    abelian TPP triple proves |A||B||C| <= |H| = 4096.
    """
    f0, f1, f2 = (full_axis(coordinate) for coordinate in range(3))
    images = {
        add(add(a_element, b_element), c_element)
        for a_element in f0
        for b_element in f1
        for c_element in f2
    }
    domain_size = len(f0) * len(f1) * len(f2)
    return domain_size, len(images)


def main():
    block_side = MODULUS - 1
    group_order = MODULUS**3
    intended_relations_per_block = block_side**3
    stpp_cubic_volume = 2 * block_side**3

    print("C07 exact STPP verification: H = (Z/16Z)^3")
    print(f"|H| = {group_order}")
    print()
    print("Definition-level six-variable relation counts")

    relation_counts = {}
    for i, j, k in product(range(2), repeat=3):
        count = stpp_relation_count(i, j, k)
        relation_counts[(i, j, k)] = count
        print(f"  (i,j,k)=({i},{j},{k}): {count}")

    for indices, count in relation_counts.items():
        if indices[0] == indices[1] == indices[2]:
            assert count == intended_relations_per_block
        else:
            assert count == 0
    print("  STPP definition: PASS")
    print(
        "  diagonal counts are exactly the intended equal-pair relations: "
        f"{intended_relations_per_block} per block"
    )

    print()
    print("Direct group-algebra embedding audit")
    embedding = audit_group_algebra_embedding()
    for key in (
        "left_support",
        "right_support",
        "output_support",
        "tested_products",
        "output_hits",
    ):
        print(f"  {key}: {embedding[key]}")
    print(f"  forbidden_aliases: {len(embedding['forbidden_aliases'])}")
    assert embedding["left_support"] == 2 * block_side**2
    assert embedding["right_support"] == 2 * block_side**2
    assert embedding["output_support"] == 2 * block_side**2
    assert embedding["output_hits"] == stpp_cubic_volume
    assert not embedding["forbidden_aliases"]
    print("  direct sum 2*<15,15,15> restriction: PASS")

    print()
    print("Exact tensor/rank/capacity arithmetic")
    print("  realized tensor: <15,15,15> direct-sum <15,15,15>")
    print(f"  cubic volume: 2*15^3 = {stpp_cubic_volume}")
    print(f"  abelian group-algebra rank: |H| = {group_order}")
    overload = Fraction(stpp_cubic_volume, group_order)
    print(
        "  cubic-volume/rank ratio: "
        f"{overload.numerator}/{overload.denominator}"
    )
    assert overload == Fraction(3375, 2048)

    single_domain, single_images = verify_single_tpp_tight_witness()
    print(
        "  tight single-TPP witness: <16,16,16>, "
        f"domain={single_domain}, distinct sums={single_images}"
    )
    assert single_domain == single_images == group_order
    assert stpp_cubic_volume > single_domain
    print(f"  STPP beats the tight single-TPP cubic cap: {stpp_cubic_volume} > {single_domain}")

    # Theorem 5.5 for abelian H gives 2*15^omega <= 4096, hence
    # omega <= log_15(2048).  The strict improvement over 3 is certified
    # entirely by the integer inequality 2048 < 15^3.
    assert group_order % 2 == 0
    asi_rhs_per_block = group_order // 2
    assert asi_rhs_per_block == 2048
    assert asi_rhs_per_block < block_side**3
    print("  ASI inequality: 2*15^omega <= 4096")
    print("  exact bound: omega <= log_15(2048) < 3")

    # Display-only decimal; not used for any gate.
    getcontext().prec = 50
    decimal_bound = Decimal(asi_rhs_per_block).ln() / Decimal(block_side).ln()
    print(f"  display decimal: {decimal_bound}")

    # Honest comparison with Strassen, proved using the rational separator 2.81:
    #   log_2(7) < 281/100 < log_15(2048).
    # Both comparisons are exact integer-power comparisons.
    assert 7**100 < 2**281
    assert 15**281 < 2048**100
    print(
        "  exact context: log_2(7) < 281/100 < log_15(2048), "
        "so this does not beat Strassen"
    )

    print()
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
