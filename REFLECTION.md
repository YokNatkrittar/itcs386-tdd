# Reflection: TDD Lab (ITCS386)

## 1. How many tests did you write in Part A, and how many lines of production code? What is the ratio?

I ended Part A with 9 tests in `test_kitchen.py`. Along the way I also wrote and deleted one test (`test_multiplication_by_two`), because the new "returns a new quantity" test already covered it. `kitchen.py` has about 59 lines in total, or about 41 lines if I do not count blank lines. So the ratio is roughly 1 test for every 4 to 5 lines of production code. I was surprised that the tests were as long as the code they checked, because I expected the code to be much bigger.

## 2. When was your bar red for the longest time, and what made it last so long?

The longest red bar was in step A5, when I added units and the factory functions `grams()` and `ounces()`. I changed the test file to import `grams` and `ounces` before I had added them to `kitchen.py`, so `pytest` kept stopping with an `ImportError`. I also pasted `pytest` and `git commit` together, so I committed while the tests were still failing, and the commit message said "refactor" even though the bar was red. I learned to run `pytest -q` alone, read the result, and only then commit. I also learned that "I saved the file" is not the same as "the function is really in the file".

## 3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right?

- **Fake It:** In A1 I made `times` set the amount to 600, and in A6 I made `plus` return `grams(500)`. This was the right choice. It felt silly, but it proved that the test setup worked, and the next test removed the fake right away.
- **Triangulate:** In A2 I added a test for 200 x 2 = 400, which forced me to replace the constant 600 with the real formula `self.amount * multiplier`. This was right. One example can always be satisfied by a constant, but two cannot.
- **Obvious Implementation:** I used this for `Sum.times` in A8 and for the real `__eq__`. The code was short and I was confident, so it was right. The tests were green on the first try, and a smaller step would have wasted time.

## 4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?

The only item left is "Quantity is unhashable (defined `__eq__` without `__hash__`)". I would implement it next only if some code needs to put a `Quantity` in a set or use it as a dictionary key. Nothing needs that now, so I left it alone. Everything else on the list is done and ticked. If I had to delete one item as speculation, it would be this one, because it comes from a possible future need and not from a real requirement. Another possible item is a missing conversion rate (a `KeyError` in `Converter.rate`), but I never wrote a test for it, so I would add it to the list first.

## 5. Look at `Quantity.reduce`. If you had designed the whole system on paper first, would you have written this method?

No, I do not think so. On paper I would probably have written one `convert(quantity, unit)` function in the converter, and `Sum` would have been a plain "add" function. I would not have thought of giving `Quantity` and `Sum` the same `reduce` method. It appeared because `Converter.reduce` needed to treat both objects in the same way, and I think it is a nicer design than mine would have been. The odd part is that `Quantity.reduce` takes a converter, so a plain quantity has to know about conversion even though the real work happens in `Converter`.

## 6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design?

Writing tests after the code (Part 0) felt like checking someone else's work. The code was already there, so I read it and tried to find bugs, and in `shipping.py` it was easy to copy the code's behaviour by mistake. I had to stay with the docstring rules, which is why the tests found the three bugs. Writing tests first (Part A) felt slower and strange at the start, but I always knew what the next small step was, and the code was never bigger than the tests needed. The tests that shaped the design most were `test_multiplication_returns_a_new_quantity`, which made `Quantity` a value object, and `test_mixed_addition`, which led to `Sum` and the converter being passed into `reduce`. I would not have found these designs by myself at the beginning.