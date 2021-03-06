mkdir data
mkdir data/preprocessed
cd data

# Download and unpack data
echo 'Unpack src files...'

if [ ! -d skonlitt_sverige_1890-99 ]; then
    wget https://efselab.s3.eu-north-1.amazonaws.com/skonlitt_sverige_1890-99.tar.gz
    tar xvzf skonlitt_sverige_1890-99.tar.gz
    rm skonlitt_sverige_1890-99.tar.gz
fi

if [ ! -d sou-2020-2021.text ]; then
    wget https://efselab.s3.eu-north-1.amazonaws.com/sou-2020-2021.text.tar.gz
    tar xvzf sou-2020-2021.text.tar.gz
    rm sou-2020-2021.text.tar.gz
fi

if [ ! -d yttr-2018-2021.text ]; then
    wget https://efselab.s3.eu-north-1.amazonaws.com/yttr-2018-2021.text.tar.gz
    tar xvzf yttr-2018-2021.text.tar.gz
    rm yttr-2018-2021.text.tar.gz
fi

if [ ! -d preprocessed_corpora ]; then
    wget https://efselab.s3.eu-north-1.amazonaws.com/preprocessed_corpora.tar.gz
    tar xvzf preprocessed_corpora.tar.gz
    rm preprocessed_corpora.tar.gz
fi



