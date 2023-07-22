abs = ['start',12, 789, 9, 'mega', 89, 35]
for i in abs:
  if isinstance(i, str):
    abs.remove(i)
print(f"Max: {max(abs)}\nMin: {min(abs)}\nSumma: {sum(abs)}")
print(abs)
#strlarni chetlab sonlar bilan ishlash