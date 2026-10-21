class LibraryDevice:
    def __init__(self, device_id):
        self.device_id = device_id

    def show_info(self):
        print(f"[LibraryDevice Info] Device ID: {self.device_id}")


class ReceiptPrinter:
    def print_receipt(self):
        print("[ReceiptPrinter] Printing transaction receipt...")


class SelfCheckoutKiosk(LibraryDevice):
    def __init__(self, device_id, location):
        super().__init__(device_id)
        self.location = location
        self.printer = ReceiptPrinter()

    def show_info(self):
        super().show_info()
        print(f"[Kiosk Info] Location: {self.location}")

    def print_kiosk_receipt(self):
        self.printer.print_receipt()


class LibraryBranch:
    def __init__(self, name):
        self.name = name
        self.kiosk = None

    def assign_kiosk(self, kiosk):
        self.kiosk = kiosk
        print(f"[LibraryBranch] Kiosk {kiosk.device_id} assigned to {self.name}.")


class BarcodeScanner:
    def scan_item(self, item):
        print(f"[BarcodeScanner] Scanned barcode for: '{item}'")


class Librarian:
    def __init__(self, name):
        self.name = name

    def check_item(self, item, scanner):
        print(f"[Librarian] {self.name} is preparing to check an item.")
        scanner.scan_item(item)
        print(f"[Librarian] {self.name} finished checking '{item}'.")

print("1. Create one SelfCheckoutKiosk")
my_kiosk = SelfCheckoutKiosk(device_id="SCK-99", location="Main Entrance Lobby")

print("2. Call the inherited show_info()")
my_kiosk.show_info()

print("3. Call a ReceiptPrinter method through the SelfCheckoutKiosk")
my_kiosk.print_kiosk_receipt()

print("4. Create a LibraryBranch and give it the existing SelfCheckoutKiosk")
central_branch = LibraryBranch("Central Library Branch")
central_branch.assign_kiosk(my_kiosk)

print("5. Delete/remove the LibraryBranch, then show that the kiosk works")
del central_branch
print("[System] LibraryBranch object deleted successfully.")

my_kiosk.show_info()

print("Create a BarcodeScanner and a Librarian")
handheld_scanner = BarcodeScanner()
librarian1 = Librarian("Boomshakalaka")

print("7. Make the Librarian check an item using the BarcodeScanner")
librarian1.check_item("The Great Gatsby", handheld_scanner)
