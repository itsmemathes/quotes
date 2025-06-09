from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Sample caption databases
captions = {
    "love": [
        "Love is not about possession, it's about appreciation.",
        "In the arithmetic of love, one plus one equals everything.",
        "The best thing to hold onto in life is each other.",
        "Love is when the other person's happiness is more important than your own.",
        "We are most alive when we're in love.",
        "Love doesn't make the world go round. Love is what makes the ride worthwhile.",
        "To love and be loved is to feel the sun from both sides.",
        "Love is composed of a single soul inhabiting two bodies.",
        "The giving of love is an education in itself.",
        "Where there is love there is life."
    ],
    "friend": [
        "A real friend is one who walks in when the rest of the world walks out.",
        "Friendship is born at that moment when one person says to another, 'What! You too? I thought I was the only one.'",
        "A friend is someone who knows all about you and still loves you.",
        "Friendship is the only cement that will ever hold the world together.",
        "Good friends are like stars. You don't always see them, but you know they're always there.",
        "There is nothing on this earth more to be prized than true friendship.",
        "A single rose can be my garden... a single friend, my world.",
        "Friends show their love in times of trouble, not in happiness.",
        "Life is partly what we make it, and partly what it is made by the friends we choose.",
        "Wishing to be friends is quick work, but friendship is a slow ripening fruit."
    ],
    "money": [
        "Money is a tool. Used properly it makes something beautiful; used improperly, it makes a mess!",
        "It's not how much money you make, but how much money you keep.",
        "The art is not in making money, but in keeping it.",
        "Money often costs too much.",
        "Formal education will make you a living; self-education will make you a fortune.",
        "Never spend your money before you have it.",
        "The safest way to double your money is to fold it over and put it in your pocket.",
        "Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver.",
        "Wealth consists not in having great possessions, but in having few wants.",
        "If money is your hope for independence you will never have it."
    ],
    "life": [
        "Life is what happens when you're busy making other plans.",
        "Get busy living or get busy dying.",
        "You only live once, but if you do it right, once is enough.",
        "In three words I can sum up everything I've learned about life: it goes on.",
        "Life is really simple, but we insist on making it complicated.",
        "The purpose of our lives is to be happy.",
        "Life is a succession of lessons which must be lived to be understood.",
        "Life is 10% what happens to us and 90% how we react to it.",
        "The biggest adventure you can take is to live the life of your dreams.",
        "Life is not a problem to be solved, but a reality to be experienced."
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_captions():
    topic = request.form.get('topic', 'love')
    count = int(request.form.get('count', 10))
    
    if topic not in captions:
        return jsonify({"error": "Topic not found"}), 404
    
    available_captions = captions[topic].copy()
    selected_captions = []
    
    for _ in range(min(count, len(available_captions))):
        if not available_captions:
            break
        caption = random.choice(available_captions)
        selected_captions.append(caption)
        available_captions.remove(caption)
    
    return jsonify({
        "topic": topic,
        "captions": selected_captions,
        "remaining": len(available_captions)
    })

if __name__ == '__main__':
    app.run(debug=True)