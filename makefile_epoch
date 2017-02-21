zcat = collaboration/zcat_epoch_$(EPOCH).fits
speclist = disk/speclist_epoch_$(EPOCH).fits
ccdlist = disk/ccdlist_epoch_$(EPOCH).fits
fibermaplist = telescope/fibermaplist_epoch_$(EPOCH).fits
mtlfile = collaboration/mtl_epoch_$(EPOCH).fits


$(zcat): $(speclist)
	touch $(zcat)

$(speclist): $(ccdlist)
	touch $(speclist)

$(ccdlist): $(fibermaplist)
	touch $(ccdlist)

$(fibermaplist): $(mtlfile)
	touch $(fibermaplist)

$(mtlfile): 
	touch $(mtlfile)

clean:
	rm -Rf collaboration/* disk/* telescope/* collaboration/*



