import pydraw

screenMain = screen(1000, 800, 'GRID-OS')
running = True
print('start')
print('')
while running:
  question1 = input('--> ')
  if question1 == end:
    screen.stop()
  else:
    print('An error occured, please try again')
