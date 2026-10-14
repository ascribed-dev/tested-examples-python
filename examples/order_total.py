# :snippet-start: order-total
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Line:
    item: str
    price: Decimal
    quantity: int


def total(lines: list[Line]) -> Decimal:
    return sum((line.price * line.quantity for line in lines), Decimal(0))


order = [
    Line("Notebook", Decimal("4.50"), 2),
    Line("Pen", Decimal("1.25"), 4),
]

for line in order:
    print(f"{line.quantity} x {line.item}")
print(f"Total: {total(order):.2f}")
# :snippet-end:
