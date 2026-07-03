from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store bids
bids = {}


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder, bid_amount in bidding_dictionary.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    return winner, highest_bid


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        bid = int(request.form["bid"])

        bids[name] = bid

        return redirect(url_for("index"))

    return render_template("index.html", bids=bids)


@app.route("/winner")
def winner():
    if not bids:
        return "No bids placed yet."

    winner_name, highest_bid = find_highest_bidder(bids)

    return render_template(
        "winner.html",
        winner=winner_name,
        amount=highest_bid
    )


@app.route("/reset")
def reset():
    bids.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)