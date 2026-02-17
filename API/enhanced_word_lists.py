# Enhanced word lists for better sentiment analysis
import pandas as pd
import os

def load_enhanced_word_lists():
    """Load enhanced word lists for sentiment analysis"""
    base_path = os.path.dirname(__file__)
    
    # Positive words list
    positive_words = [
        'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'love', 'like', 'enjoy',
        'happy', 'pleased', 'satisfied', 'impressed', 'awesome', 'perfect', 'best', 'nice',
        'beautiful', 'brilliant', 'outstanding', 'superb', 'magnificent', 'delightful'
    ]
    
    # Negative words list  
    negative_words = [
        'bad', 'terrible', 'awful', 'horrible', 'hate', 'dislike', 'worst', 'ugly',
        'disgusting', 'pathetic', 'useless', 'worthless', 'disappointed', 'annoying',
        'frustrating', 'disappointing', 'poor', 'unacceptable', 'inadequate'
    ]
    
    # Bad words list (strong negative)
    bad_words = [
        'fuck', 'shit', 'damn', 'hell', 'bitch', 'asshole', 'bastard', 'crap',
        'goddamn', 'motherfucker', 'son_of_bitch', 'whore', 'slut', 'dickhead'
    ]
    
    return {
        'positive_words': positive_words,
        'negative_words': negative_words, 
        'bad_words': bad_words
    }

def enhanced_sentiment_score(text, word_lists):
    """Calculate enhanced sentiment score using word lists"""
    words = text.lower().split()
    positive_count = sum(1 for word in words if word in word_lists['positive_words'])
    negative_count = sum(1 for word in words if word in word_lists['negative_words'])
    bad_count = sum(1 for word in words if word in word_lists['bad_words'])
    
    # Weighted scoring
    score = (positive_count * 1.0) - (negative_count * 1.0) - (bad_count * 2.0)
    
    # Normalize score
    total_words = len([w for w in words if w.isalpha()])
    if total_words > 0:
        score = score / total_words
    
    return {
        'score': score,
        'positive_count': positive_count,
        'negative_count': negative_count,
        'bad_count': bad_count,
        'sentiment': 'positive' if score > 0.1 else 'negative' if score < -0.1 else 'neutral'
    }
