.PHONY: sound image

augustin.jpg:
	wget -O augustin.jpg https://upload.wikimedia.org/wikipedia/commons/0/03/Sandro_Botticelli_050.jpg

augustin.ppm: augustin.jpg
	convert augustin.jpg augustin.ppm

sound:
	aplay output/augustin.ppm
image:
	feh output/augustin.ppm
