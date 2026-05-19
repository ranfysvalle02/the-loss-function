import time

class NarrativeModel:
    def __init__(self, name, initial_bias, initial_weight, learning_rate=0.20):
        self.name = name
        self.bias = initial_bias       # Baseline Trust (Internal Disposition)
        self.weight = initial_weight   # Vulnerability Weight (Signal Sensitivity)
        self.learning_rate = learning_rate

    def predict(self, signal):
        return max(0.0, min(1.0, (signal * self.weight) + self.bias))

    def update(self, signal, pred, actual):
        error = pred - actual
        # Gradient updates
        self.bias -= self.learning_rate * (2 * error)
        self.weight -= self.learning_rate * (2 * error * signal)
        # Regularization / Boundary control
        self.bias = max(0.0, min(1.0, self.bias))
        self.weight = max(0.0, min(1.0, self.weight))

def run_story():
    # Standard ANSI colors for terminal beauty
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    alex = NarrativeModel("Alex", initial_bias=0.15, initial_weight=0.20)

    timeline = [
        {"signal": 0.8, "actual": 0.85, "context": "A new friend returns a vulnerable text quickly."},
        {"signal": 0.7, "actual": 0.90, "context": "A coworker proactively offers help on a tough day."},
        {"signal": 0.9, "actual": 0.85, "context": "A partner remembers a small, specific preference."},
        {"signal": 0.2, "actual": 0.10, "context": "A stranger bumps past rudely on the subway corridor."},
        {"signal": 0.8, "actual": 0.95, "context": "A mentor explicitly defends Alex's work in a high-stakes meeting."}
    ]

    print(f"{BOLD}{CYAN}============ SYSTEM INITIALIZATION: SYSTEM INTERNALS LOG ============{RESET}")
    print(f"Subject       : Alex")
    print(f"Historical Dataset : Chronic relational volatility; defense optimization.")
    print(f"Current State : Overfit to past trauma. System assumes threat by default.")
    print(f"{CYAN}====================================================================={RESET}\n")
    time.sleep(1.5)

    for day, exp in enumerate(timeline, 1):
        # -----------------------------------------------------------------
        # PHASE 1: THE MORNING POSTURE (Priors)
        # -----------------------------------------------------------------
        print(f"{BOLD}--- [DAY {day}: THE LOOP BEGINS] ---{RESET}")
        print(f"  {BOLD}The Morning Posture (Internal Settings):{RESET}")
        print(f"    • Baseline Trust (Bias)  : {alex.bias:.2f} -> ", end="")
        if alex.bias < 0.3: print(f"{RED}Defensive shell. Expecting coldness.{RESET}")
        elif alex.bias < 0.5: print(f"{YELLOW}Cautious. Testing the perimeter.{RESET}")
        else: print(f"{GREEN}Open. Allowing the possibility of safety.{RESET}")
        
        print(f"    • Sensitivity (Weight)   : {alex.weight:.2f} (How much external proof Alex requires)")
        print("")
        time.sleep(1.0)

        # -----------------------------------------------------------------
        # PHASE 2: THE ENCOUNTER (Data Input)
        # -----------------------------------------------------------------
        print(f"  {BOLD}The Event (External Input):{RESET}")
        print(f"    \"{exp['context']}\"")
        
        pred = alex.predict(exp['signal'])
        loss = (pred - exp['actual']) ** 2
        
        print(f"    • Predicted Safety : {pred:.2f}")
        print(f"    • Actual Safety    : {exp['actual']:.2f}")
        time.sleep(1.0)

        # -----------------------------------------------------------------
        # PHASE 3: THE COLLISION (Loss Evaluation)
        # -----------------------------------------------------------------
        print(f"\n  {BOLD}The Internal Collision (Dissonance Calculation):{RESET}")
        print(f"    • Loss Score : {loss:.4f}")
        
        if loss > 0.05:
            if exp['actual'] > pred:
                print(f"    {YELLOW}⚠️  POSITIVE SURPRISE SPIKE:{RESET} Reality was kinder than the model predicted.")
                print(f"       Internal Monologue: 'They actually care? Why would they do that? This doesn't fit my code.'")
            else:
                print(f"    {RED}🚨 COMPULSIVE REGRESSION SPIKE:{RESET} A negative data point matches the old childhood dataset.")
                print(f"       Internal Monologue: 'I knew it. See? Trusting people is a design flaw.'")
        else:
            print(f"    {GREEN}✅ LOW DISSONANCE:{RESET} Reality aligns with expectations. The nervous system settles.")
            print(f"       Internal Monologue: 'Okay. This makes sense. We are safe right here.'")
        
        time.sleep(1.2)

        # -----------------------------------------------------------------
        # PHASE 4: THE NIGHT SHIFT (The Gradient Descent Update)
        # -----------------------------------------------------------------
        old_bias, old_weight = alex.bias, alex.weight
        alex.update(exp['signal'], pred, exp['actual'])
        
        print(f"\n  {BOLD}The Night Shift (Parameter Re-tuning):{RESET}")
        print(f"    Trimming error. Running optimization over the day's footprints...")
        print(f"    • Bias Shift   : {old_bias:.2f} -> {alex.bias:.2f}")
        print(f"    • Weight Shift : {old_weight:.2f} -> {alex.weight:.2f}")
        print(f"    {CYAN}Status: Model parameters updated. Sleeping...{RESET}\n")
        print("-" * 60 + "\n")
        time.sleep(2.0)

    # -----------------------------------------------------------------
    # FINAL EVALUATION
    # -----------------------------------------------------------------
    print(f"{BOLD}{GREEN}============ POST-TRAINING METRICS SUMMARY ============{RESET}")
    print(f"Alex's Final Baseline Trust (Bias): {alex.bias:.2f} (Up from 0.15)")
    print(f"Alex's Final Sensitivity (Weight) : {alex.weight:.2f} (Up from 0.20)")
    print(f"-------------------------------------------------------")
    print(f"{BOLD}Narrative Analysis:{RESET}")
    print("Alex did not delete the old memories. The original training data remains.")
    print("Instead, through 5 consecutive days of raw, courageous living, Alex")
    print("forced the nervous system to process reality exactly as it arrived.")
    print("")
    print("Notice Day 4: A random subway jerk caused a massive defensive relapse.")
    print("But because the learning rate was healthy, a single bad day didn't")
    print("destroy the progress. Day 5 corrected the course.")
    print("")
    print(f"{BOLD}{CYAN}The model is running. The next update is yours.{RESET}")
    print(f"{GREEN}======================================================={RESET}\n")

if __name__ == "__main__":
    run_story()
