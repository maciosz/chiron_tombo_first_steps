import h5py
import numpy as np

# create fast5 file from files chiron used to train model

lambda_read = h5py.File("Read_1.fast5", "w")
lambda_read.create_group("Raw")
lambda_read.create_group("Raw/Reads")
lambda_read.create_group("Raw/Reads/Read_1")
sygnal = open("train/Lambda_0001.signal")
sygnal = sygnal.readlines()
sygnal = sygnal[0].strip().split()
sygnal = [int(i) for i in sygnal]
sygnal = np.array(sygnal)
lambda_read.create_dataset("Raw/Reads/Read_1/Signal", data=sygnal)
lambda_read.create_group("UniqueGlobalKey")
lambda_read.create_group("UniqueGlobalKey/tracking_id")
lambda_read.create_group("UniqueGlobalKey/context_tags")
lambda_read.create_group("UniqueGlobalKey/channel_id")
lambda_read.create_group("PreviousReadInfo")
lambda_read['Raw']['Reads']['Read_1'].attrs['read_number'] = 1
lambda_read.close()
