obj-m   := lockup.o

KDIR    := /lib/modules/$(shell	uname -r)/build
PWD     := $(shell pwd)

lockup:
	$(MAKE) -C $(KDIR) SUBDIRS=$(PWD) modules
	
default:
	$(MAKE) -C $(KDIR) SUBDIRS=$(PWD) modules

clean:
	rm -rf *.ko
	rm -rf *.mod.*
	rm -rf .*.cmd
	rm -rf *.o
	rm -rf *.mod.c
	rm -rf *.order
	rm -rf *.symvers 
	rm -rf .tmp_versions 
