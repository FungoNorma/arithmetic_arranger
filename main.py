
from pytest import main

from arithmetic_arranger import arithmetic_arranger


problems2 = ["45 + 10", "99 - 456", "8181 + 8182", "123 - 111"]
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

problems2 = ["45 + 10", "99 - 456", "8181 + 8182", "123 - 111"]
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))


main()
