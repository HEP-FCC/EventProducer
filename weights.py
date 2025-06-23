import glob
import uproot
import os

# List of directories you want to process
directories = [
    "/eos/home-o/oarakji/tth/myRoot/fcc_v07/II/mgp8_pp_tth_5f_50TeV",
    "/eos/home-o/oarakji/tth/myRoot/fcc_v07/II/mgp8_pp_ttyy_5f_50TeV",
]

for directory in directories:
    print(f"\nProcessing directory: {directory}")
    file_pattern = os.path.join(directory, "events_*.root")
    file_list = glob.glob(file_pattern)

    total_events = 0
    total_weight = 0.0

    for filename in file_list:
        with uproot.open(filename) as f:
            tree = f["events"]  # Change if your tree name is different
            n_events = tree.num_entries
            weights = tree["EventHeader.weight"].array(library="np")
            sum_of_weights = weights.sum()
            print(f"  {os.path.basename(filename)}: events={n_events}, sum_of_weights={sum_of_weights}")
            total_events += n_events
            total_weight += sum_of_weights

    print(f"Total number of events in all files: {total_events}")
    print(f"Total sum of weights in all files: {total_weight}")