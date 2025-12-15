import tkinter as tk
from knapsack import Knapsack

wt = [1,3,4]
val = [10,40,50]
W = 5
n = len(wt)

ks = Knapsack(n, W, wt, val)

selected = [False]*n
curr_wt = 0
curr_val = 0


# GUI Window

root= tk.Tk()
root.title("0/1 Knapsack Game")
root.geometry("1000x1000")

# Title 

title = tk.Label(
    root,
    text = "0/1 knapsack Solver",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# Capacity Label

cap_label = tk.Label(
    root,
    text=f"Knapsack Capacity: {W}",
    font =("Arial", 12)

)
cap_label.pack(pady=5)

# Weights and Values

stat_label = tk.Label(
    root,
    text ="Weight: 0 | Value: 0",
    font=("Arial", 12),
    fg = "blue"
)
stat_label.pack(pady=10)

# Update stats function
def update_stats():
    stat_label.config(
        text= f"Weight: {curr_wt} | Value: {curr_val}"
    )

# Item Toggle logic:
def toggle_item(i):
    global curr_wt, curr_val

    if selected[i]:
        # Deselect item
        selected[i] = False
        curr_wt -= wt[i]
        curr_val -= val[i]
        buttons[i].config(text="Select")
    else:
        # Try select
        if curr_wt+wt[i] <= W:
            selected[i] = True
            curr_wt += wt[i]
            curr_val += val[i]
            buttons[i].config(text="Remove")
        else:
            stat_label.config(
                text=" ❌ Capacity Exceeded!",
                fg="red"
            )
            root.after(1000,update_stats)
            return

    update_stats()

# Items Frame:

it_frame = tk.Frame(root)
it_frame.pack(pady=10)

buttons = []

for i in range(n):
    frame = tk.Frame(it_frame, relief="ridge", borderwidth=2, padx=10,pady=5)
    frame.pack(pady=5, fill="x")

    label = tk.Label(
        frame,
        text=f"Item {i+1} | Weight: {wt[i]} | Value: {val[i]}",
        font=("Arial", 11)
    )
    label.pack(side ="left")

    btn = tk.Button(
        frame,text="Select",
        width=10,
        command=lambda i=i: toggle_item(i)
    )
    btn.pack(side="right")
    buttons.append(btn)
    

# Player Result:
player_label = tk.Label(
    root,
    text="Your Selection Value: 0",
    font=("Arial", 14),
    fg="green"
)
player_label.pack(pady=15)

def finalize_selection():
    player_label.config(
        text=f"Your Selection Value: {curr_val}"
    )
    compare_with_optimal()

final_btn = tk.Button(
    root,
    text="Finalize Selection",
    width=25,
    command=finalize_selection
)
final_btn.pack(pady=5)

def compare_with_optimal():
    optimal = ks.kpTab()

    if curr_val == optimal:
        res_text = (
            f"Your Value: {curr_val}\n"
            f"Optimal Value: {optimal}\n"
            f"🎉 Perfect! You found the optimal solution!"
        )
        res_label.config(fg = "green")
    else:
        res_text =(
            f"Your Value: {curr_val}\n"
            f"Optimal Value: {optimal}\n"
            f"😞 Try Again to reach the optimal solution."
        )
        res_label.config(fg="red")

    res_label.config(text=res_text)

def reset_game():
    global curr_wt, curr_val 

    curr_wt = 0
    curr_val = 0

    for i in range(n):
        selected[i] = False
        buttons[i].config(text="Select")

    # Reset stats and labels
    stat_label.config(
        text="Weight: 0 | Value: 0",
        fg="blue"
    )

    player_label.config(
        text="Your Selection Value: 0",
        fg="green"
    )


    res_label.config(text="", fg = "black")

    ks.reset_t()


# def solve_rec():
#     res = ks.kpRec(n,W)
#     res_label.config(text=f"Result (Recursion): {res}")

# def solve_memo():
#     ks.reset_t()
#     res = ks.kpMem(n,W)
#     res_label.config(text=f"Result (Memoization): {res}")

# def solve_tab():
#     res = ks.kpTab()
#     res_label.config(text=f"Result (Tabulation): {res}")    

# # Buttons

# btn_rec = tk.Button(
#     root,
#     text = "Solve using Recursion",
#     width=25,
#     command=solve_rec

# )
# btn_rec.pack(pady=5)

# btn_mem = tk.Button(
#     root,
#     text = "Solve using Memoization",
#     width=25,
#     command=solve_memo
# )
# btn_mem.pack(pady=5)

# btn_tab = tk.Button(
#     root,
#     text= "Solve using Tabulation",
#     width=25,
#     command=solve_tab
# )
# btn_tab.pack(pady=5)

res_label = tk.Label(
    root,
    text="",
    font=("Arial", 13),
    justify="center"
)
res_label.pack(pady=10)

reset_btn = tk.Button(
    root,
    text="Reset Game",
    width=25,
    bg ='#f44336',
    fg='white',
    command=reset_game
)
reset_btn.pack(pady=10)

# start GUI

root.mainloop()

