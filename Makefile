augustin.jpg:
    wget -O augustin.jpg https://upload.wikimedia.org/wikipedia/commons/0/03/Sandro_Botticelli_050.jpg

augustin.ppm: augustin.jpg
    convert augustin.jpg augustin.ppm
