import uproot
print('tth')
with uproot.open("/eos/home-o/oarakji/tth/myRoot/fcc_v07/II/mgp8_pp_tth_5f_50TeV/events_020084048.root") as f:
    tree = f["events"]
    weights = tree["RecoMCLink.weight"].array()
    for i, event_weights in enumerate(weights):
        print(f"Event {i}, weights: {event_weights}")
print('ttyy')
with uproot.open("/eos/home-o/oarakji/tth/myRoot/fcc_v07/II/mgp8_pp_ttyy_5f_50TeV/events_002212788.root") as f:
    tree = f["events"]
    weights = tree["RecoMCLink.weight"].array()
    for i, event_weights in enumerate(weights):
        print(f"Event {i}, weights: {event_weights}")