"""간단한 계산기"""


def apply_discount(price, rate):
    """가격에서 할인율(rate, 0~1)만큼 뺀 값을 반환한다."""
    return price * (1 - rate)


def main():
    print(apply_discount(20000, 0.15))


if __name__ == "__main__":
    main()
