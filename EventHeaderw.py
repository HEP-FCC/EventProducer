import uproot

with uproot.open("/eos/home-o/oarakji/tth/myRoot/fcc_v07/II/mgp8_pp_tth_5f_50TeV/events_020084048.root") as f:
    tree = f["events"]  # replace with your tree name if different
    weights = tree["EventHeader.weight"].array(library="np")
    print("First event weight for tth:", weights[0])

with uproot.open("/eos/home-o/oarakji/tth/myRoot/fcc_v07/II/mgp8_pp_ttyy_5f_50TeV/events_002212788.root") as f:
    tree = f["events"]  # replace with your tree name if different
    weights = tree["EventHeader.weight"].array(library="np")
    print("First event weight for ttyy:", weights[0])