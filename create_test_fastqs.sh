mkdir lambda_fastq
for i in $(seq 1 9)
do
    plik="lambda_fastq/Read_${i}.fastq"
    echo "@Read_${i}" > $plik
    cut -d' ' -f3 train/Lambda_000${i}.label | tr "\n" " " | tr -d " " >> ${plik}_tmp
    cat ${plik}_tmp >> $plik
    echo >> $plik
    echo "+Read_${i}" >> ${plik}
    # fake'owe quality scores
    cat ${plik}_tmp >> $plik
    rm ${plik}_tmp
done
