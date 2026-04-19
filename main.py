from elt import run_elt
from etl import run_etl

def main():
    choice = input("Run ETL or ELT? (etl/elt): ")
    if choice == 'etl':
        run_etl()
    elif choice == 'elt':
        run_elt()

if __name__ == '__main__':
    main()