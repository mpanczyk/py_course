#!/usr/bin/env python
# coding: utf-8

import Tkinter as tk
import tkFont

class CalcApplication(tk.Frame, object):
  
  ''' Klasa implementująca prosty kalkulator.
  '''

  ROWS = 5
  COLUMNS = 5
  BUTTON_WIDTH = 5
  BUTTON_HEIGHT = 5
  DISPLAY_FONT_SIZE = 16
  
  def __init__(self, master=None):
    super(CalcApplication, self).__init__(master)
    self.pack()
    self.setupControls()

  def setupControls(self):
    ''' Metoda inicjująca elementy wizualne.
    '''
    self.setupFuncControls()
    self.setupDisplay()
    self.setupGrid()

  def setupGrid(self):
    ''' Metoda, która sprawia,
        że przyciski mogą zmieniać swój rozmiar.
    '''
    for row in range(self.ROWS+1):
      tk.Grid.rowconfigure(self, row, weight=1)
    for column in range(self.COLUMNS):
      tk.Grid.columnconfigure(self, column, weight=1)

  def setupDisplay(self):
    ''' Metoda inicjująca widget wyświetlający
    '''
    font = tkFont.Font(size=self.DISPLAY_FONT_SIZE)
    self.display = tk.Entry(
      self,
      font=font,
      width=15,
    )
    self.display.grid(
      row=0,
      column=0,
      columnspan=3,
    )

  def setupFuncControls(self):
    ''' Metoda inicjująca przyciski.
    '''
    actions = [
      # lista krotek, z których każda to:
      # (
      #   'wyświetlany na przycisku napis',
      #   'rodzaj przycisku',
      #   'skojarzona wartość',
      #   'umiejscowienie:
      #     (
      #       wiersz,
      #       kolumna,
      #       ile_wierszy,
      #       ile_kolumn
      #    )'
      # )
      ('0',  'digit', '0',        (4,0,1,2)),
      ('1',  'digit', '1',        (3,0,1,1)),
      ('2',  'digit', '2',        (3,1,1,1)),
      ('3',  'digit', '3',        (3,2,1,1)),
      ('4',  'digit', '4',        (2,0,1,1)),
      ('5',  'digit', '5',        (2,1,1,1)),
      ('6',  'digit', '6',        (2,2,1,1)),
      ('7',  'digit', '7',        (1,0,1,1)),
      ('8',  'digit', '8',        (1,1,1,1)),
      ('9',  'digit', '9',        (1,2,1,1)),
      ('+',  'fun',   'plus',     (1,3,1,1)),
      ('-',  'fun',   'minus',    (1,4,1,1)),
      ('*',  'fun',   'multiply', (2,3,1,1)),
      ('/',  'fun',   'divide',   (2,4,1,1)),
      ('**', 'fun',   'power',    (3,3,1,2)),
      ('=',  'fun',   'evaluate', (4,3,1,1)),
      ('AC', 'fun',   'clear',    (4,4,1,1)),
    ]
    for (label, action_type, action, (row, col, row_span, col_span)) in actions:
      tk.Button(
        self,
        text=label,
        # lambda wyrażenie, ponieważ funkcja on_click
        # ma się wykonać dopiero w momencie kliknięcia,
        # a nie teraz.
        command=lambda action_type=action_type, action=action:
          self.on_click( (action_type, action) ),
        width=self.BUTTON_WIDTH*col_span,
        height=self.BUTTON_HEIGHT*row_span,
      ).grid(
        row=row,
        column=col,
        rowspan=row_span,
        columnspan=col_span,
        sticky=tk.N+tk.S+tk.E+tk.W,
      )

  def do_action(self, action):
    ''' Metoda wywoływana po aktywacji
        przycisku funkcyjnego (czyli innego, niż cyfra).
    '''
    # TODO: tutaj trzeba dokończyć
    print action

  def insert_digit(self, digit):
    ''' Metoda wywoływana po aktywacji
        przycisku z cyfrą.
    '''
    # TODO: tutaj trzeba dokończyć
    print digit
    self.display.insert(tk.END, digit)

  def on_click(self, action):
    ''' Metoda wywoływana po aktywacji przycisku.
    '''
    action_type, value = action
    if action_type == 'digit':
      self.insert_digit(value)
    elif action_type == 'fun':
      self.do_action(value)

def main():
  calc = tk.Tk()
  calc.title("Prosty Kalkulator")
  app = CalcApplication(master=calc)
  app.mainloop()

if __name__ == '__main__':
  main()
