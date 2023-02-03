from services.rsa_service import RSA_Service
from ui.ui import UI
from ui.console_io import Console_IO

def main():
    console_io = Console_IO()
    rsa_service = RSA_Service()
    ui = UI(console_io, rsa_service)
    ui.run()

if __name__ == "__main__":
    main()