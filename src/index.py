from services.message_service import Message_Service
from services.rsa_service import RSA_Service
from services.algorithm_service import Algorithm_Service
from ui.ui import UI
from ui.console_io import Console_IO

def main():
    console_io = Console_IO()
    algorithm_service = Algorithm_Service()
    rsa_service = RSA_Service(algorithm_service)
    message_service = Message_Service()
    ui = UI(console_io, message_service, rsa_service)
    ui.run()

if __name__ == "__main__":
    main()
    