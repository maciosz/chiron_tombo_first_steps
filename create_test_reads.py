import h5py
import numpy as np

# create fast5 files from files chiron used to train model
# for reads 1 - 9

for i in range(1, 10):
    lambda_read = h5py.File("lambda_fast5/Read_" + str(i) + ".fast5", "w")
    lambda_read.create_group("Raw")
    lambda_read.create_group("Raw/Reads")
    lambda_read.create_group("Raw/Reads/Read_" + str(i))
    sygnal = open("train/Lambda_000" + str(i) + ".signal")
    sygnal = sygnal.readlines()
    sygnal = sygnal[0].strip().split()
    sygnal = [int(j) for j in sygnal]
    sygnal = np.array(sygnal)
    lambda_read.create_dataset("Raw/Reads/Read_" + str(i) + "/Signal", data=sygnal)
    lambda_read.create_group("UniqueGlobalKey")
    lambda_read.create_group("UniqueGlobalKey/tracking_id")
    lambda_read.create_group("UniqueGlobalKey/context_tags")
    lambda_read.create_group("UniqueGlobalKey/channel_id")
    # jakies wartosci z losowego reada
    # nie rozumiem ich ale sadze ze do testowania nie musze
    # ocz. do wlasciwego trenowania powinny byc dobre,
    # ale we wlasciwych readach, nie tworzonych sztucznie, sa podane
    channel_id_attrs = {'channel_number': 170,
                        'offset': 18.0,
                        'range': 1485.56,
                        'digitisation': 8192.0,
                        'sampling_rate': 4000.0}
    for key, value in channel_id_attrs.items():
        lambda_read["UniqueGlobalKey/channel_id"].attrs[key] = value
    lambda_read.create_group("PreviousReadInfo")
    lambda_read['Raw']['Reads']["Read_" + str(i)].attrs['read_number'] = i
    lambda_read.close()
