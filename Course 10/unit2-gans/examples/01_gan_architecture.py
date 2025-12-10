"""
Unit 2 - Example 1: GAN Architecture
الوحدة 2 - مثال 1: هيكل GAN

This example demonstrates:
1. GAN architecture components
2. Generator and Discriminator
3. Adversarial training concept
4. Loss functions
"""

import numpy as np

print("=" * 60)
print("Example 1: GAN Architecture")
print("مثال 1: هيكل GAN")
print("=" * 60)

# 1. GAN Components
# مكونات GAN
print("\n1. GAN Architecture")
print("هيكل GAN")
print("-" * 60)

gan_explanation = """
GAN consists of two networks:

Generator (المولد):
- Takes random noise as input
- Generates fake data
- Tries to fool the discriminator
- Goal: Generate realistic data

Discriminator (المميز):
- Takes real or fake data as input
- Classifies as real or fake
- Tries to distinguish real from fake
- Goal: Correctly identify fake data

Training Process:
- Generator and Discriminator compete
- Generator improves to create better fakes
- Discriminator improves to detect fakes
- Equilibrium: Generator creates perfect fakes
"""

print(gan_explanation)

# 2. Simple Generator Example
# مثال بسيط على المولد
print("\n" + "=" * 60)
print("2. Generator Network")
print("شبكة المولد")
print("=" * 60)

def simple_generator(noise, weights):
    """
    Simple generator that transforms noise to data.
    مولد بسيط يحول الضوضاء إلى بيانات.
    """
    # Simulate: noise -> hidden -> output
    hidden = noise * weights[0]
    output = hidden * weights[1]
    return output

# Example: Generate fake data
noise = np.random.randn(10)  # Random noise
weights = [2.0, 1.5]  # Generator weights
fake_data = simple_generator(noise, weights)

print(f"\nInput noise shape: {noise.shape}")
print(f"Generated fake data shape: {fake_data.shape}")
print(f"Sample fake data: {fake_data[:5]}")

# 3. Simple Discriminator Example
# مثال بسيط على المميز
print("\n" + "=" * 60)
print("3. Discriminator Network")
print("شبكة المميز")
print("=" * 60)

def simple_discriminator(data, threshold=0.5):
    """
    Simple discriminator that classifies real vs fake.
    مميز بسيط يصنف الحقيقي مقابل المزيف.
    """
    # Simple rule: if data > threshold, likely real
    probability = 1 / (1 + np.exp(-np.mean(data)))
    prediction = "real" if probability > threshold else "fake"
    return prediction, probability

# Test discriminator
real_data = np.random.randn(10) + 2  # Real data (shifted)
fake_data = np.random.randn(10) - 2  # Fake data (shifted)

real_pred, real_prob = simple_discriminator(real_data)
fake_pred, fake_prob = simple_discriminator(fake_data)

print(f"\nReal data: {real_pred} (probability: {real_prob:.3f})")
print(f"Fake data: {fake_pred} (probability: {fake_prob:.3f})")

# 4. Adversarial Training Concept
# مفهوم التدريب التنافسي
print("\n" + "=" * 60)
print("4. Adversarial Training")
print("التدريب التنافسي")
print("=" * 60)

training_concept = """
Adversarial Training Process:

Step 1: Train Discriminator
- Show real data → Discriminator learns real patterns
- Show fake data → Discriminator learns to detect fakes

Step 2: Train Generator
- Generate fake data
- Try to fool discriminator
- Update generator to create better fakes

Step 3: Repeat
- Discriminator gets better at detection
- Generator gets better at generation
- Both improve together

This creates a competitive learning environment!
"""

print(training_concept)

# 5. Loss Functions
# دوال الخسارة
print("\n" + "=" * 60)
print("5. GAN Loss Functions")
print("دوال خسارة GAN")
print("=" * 60)

loss_explanation = """
Generator Loss:
- Wants to maximize discriminator's error on fake data
- Loss = -log(D(fake_data))

Discriminator Loss:
- Wants to correctly classify real and fake
- Loss = -log(D(real_data)) - log(1 - D(fake_data))

Minimax Game:
- Generator minimizes its loss
- Discriminator minimizes its loss
- Nash equilibrium when both are optimal
"""

print(loss_explanation)

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
print("\nNote: For actual implementation, use TensorFlow/Keras or PyTorch")
print("ملاحظة: للتنفيذ الفعلي، استخدم TensorFlow/Keras أو PyTorch")

