#!/usr/bin/env python3

from pwn import *

# Target
HOST = "154.57.164.71"
PORT = 30572

def main():
    # Remote connection
    io = remote(HOST, PORT)

    # Agar local test qilmoqchi bo‘lsang:
    # io = process("./binary")

    # Debug (kerak bo‘lsa)
    # context.log_level = 'debug'

    # Serverdan kelayotgan banner
    print(io.recvline().decode())

    # 👇 Bu yerda challenge logikasini yozamiz
    # Misol uchun input yuborish:
    # io.sendline(b"test")

    # Response olish
    # response = io.recvline()
    # print(response)

    # Interactive mode (qo‘lda ishlash uchun)
    io.interactive()


if __name__ == "__main__":
    main()
