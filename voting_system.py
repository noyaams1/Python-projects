voters = [
    {"name": "Noya", "age": 24, "address": "Herzl 12, Tel Aviv", "has_voted": False},
    {"name": "Itay", "age": 31, "address": "Begin 7, Haifa", "has_voted": False},
    {"name": "Lior", "age": 45, "address": "Weizmann 3, Ramat Gan", "has_voted": False},
    {"name": "Maya", "age": 66, "address": "Shenkar 9, Holon", "has_voted": False},
    {"name": "Avi", "age": 70, "address": "Dizengoff 22, Netanya", "has_voted": False},
]

candidates = [
    {"name": "Alice Cohen", "position": "President"},
    {"name": "David Levy", "position": "Vice President"},
    {"name": "Sara Ben-Haim", "position": "Treasurer"},
    {"name": "Yoni Abramov", "position": "Secretary"},
    {"name": "Rina Gold", "position": "President"},
    {"name": "Tom Hadad", "position": "Vice President"},
    {"name": "Yoni Abramov", "position": "Treasurer"},
    {"name": "David Levy", "position": "President"},
]

votes_lst = []
vote_count = {}

# Display list of candidates
print("List of Candidates:")
for i, candidate in enumerate(candidates):
    print(f"{i}: {candidate['name']} - {candidate['position']}")

# Voting function
def votes(voters, votes_lst):
    for voter in voters:
        if not voter["has_voted"]:
            print(f"\nHello {voter['name']}, please cast your vote.")
            try:
                choice = int(input(f"Choose candidate (0 - {len(candidates)-1}): "))
                if 0 <= choice < len(candidates):
                    selected = candidates[choice]
                    votes_lst.append({"ID": voter["name"], "vote": selected})
                    voter["has_voted"] = True
                    name = selected["name"]
                    vote_count[name] = vote_count.get(name, 0) + 1
                    print(f"Vote for {name} recorded.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")
        else:
            print(f"{voter['name']}, you already voted.")
    return votes_lst

# Start voting process
votes(voters, votes_lst)

# Display final results
print("\nFinal Vote Count:")
for name, count in vote_count.items():
    print(f"{name}: {count} vote(s)")
