from calculator import add


def main() -> None:
    actual = add(2, 3)
    if actual != 5:
        raise AssertionError(f"expected 5, got {actual}")


if __name__ == "__main__":
    main()
