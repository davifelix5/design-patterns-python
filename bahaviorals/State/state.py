"""
Determina diferentes modos de operação para o método de uma classe dependendo
do estado em que a classe está
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class OrderState(ABC):

    def __init__(self, order: Order) -> None:
        self.order = order

    def show_state(self):
        print('Current State: ', self.order.state)
        print()

    @abstractmethod
    def handle_pending(self) -> None: pass

    @abstractmethod
    def handle_approve(self) -> None: pass

    @abstractmethod
    def handle_reject(self) -> None: pass

    def __str__(self):
        return self.__class__.__name__


class PaymentPending(OrderState):

    def handle_pending(self):
        print('Your payment is pending already')
        self.show_state()

    def handle_approve(self):
        print('Payment approved')
        self.order.state = PaymentApproved(self.order)
        self.show_state()

    def handle_reject(self):
        print('Payment rejected')
        self.order.state = PaymentRejected(self.order)
        self.show_state()


class PaymentApproved(OrderState):

    def handle_pending(self):
        print('Payment pending')
        self.order.state = PaymentPending(self.order)
        self.show_state()

    def handle_approve(self):
        print('Your payment is approved already')
        self.show_state()

    def handle_reject(self):
        print('Payment rejected')
        self.order.state = PaymentRejected(self.order)
        self.show_state()


class PaymentRejected(OrderState):

    def handle_pending(self):
        print('You payment has already been refused!')
        self.show_state()

    def handle_approve(self):
        print('You payment has already been refused!')
        self.show_state()

    def handle_reject(self):
        print('You payment has already been refused!')
        self.show_state()


class Order:
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        self.state.handle_pending()

    def approve(self):
        self.state.handle_approve()

    def reject(self):
        self.state.handle_reject()


if __name__ == "__main__":
    order = Order()
    order.reject()
    order.approve()
    order.pending()
