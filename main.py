from router.router import Router


def main():

    router = Router()

    print("=" * 50)
    print("Personal JARVIS v0.1")
    print("Type 'quit' to exit.")
    print("=" * 50)

    while True:

        request = input("\nYou: ").strip()

        if not request:
            continue

        if request.lower() == "quit":
            print("\nGoodbye!")
            break

        intent = router.route(request)

        print(f"\nDetected Intent : {intent.name}")


if __name__ == "__main__":
    main()