
MSCN = '\"2348050002161\"'
VLR = '\"2348050002161\"'
ZERO_DPC = '000000'


def print_gci(filehandler, **kwargs) -> None:

    print(f'ADD LAIGCI: GCI="{kwargs["gci"]}", LAIGCINAME="{kwargs["laigci_name"]}",MSCVLRTYPE=MSCVLRNUM,'
          f'MSCN={MSCN}, VLRN={VLR}, NONBCLAI=NO, LAICAT=GCI, LAIT=HVLR,'
          f'LOCNONAME=\"INVALID\", BSCNI1=NAT, BSCDPC1=\"{kwargs["dpc"][4:]}\", CSNAME=\"{kwargs["cs_name"]}\",'
          f'TONENAME=\"INVALID\", CELLGROUPNAME=\"INVALID\", TZDSTNAME=\"INVALID\",'
          f'LOCATIONIDNAME=\"INVALID\", E911PHASE=INVALID;', file=filehandler)


def print_sai(filehandler, **kwargs) -> None:

    print(f'ADD LAISAI: SAI="{kwargs["sai"]}", LAISAINAME="{kwargs["laisai_name"]}", PROXYLAI=NO, MSCVLRTYPE=MSCVLRNUM,'
          f'MSCN={MSCN}, VLRN={VLR}, NONBCLAI=NO, LAICAT=SAI, LAIT=HVLR, LOCNONAME=\"INVALID\",'
          f'RNCID1={kwargs["rncid"]}, CSNAME=\"{kwargs["cs_name"]}\", TONENAME=\"INVALID\", CELLGROUPNAME=\"INVALID\",'
          f'TZDSTNAME=\"INVALID\", LOCATIONIDNAME=\"INVALID\", E911PHASE=INVALID;', file=filehandler)
