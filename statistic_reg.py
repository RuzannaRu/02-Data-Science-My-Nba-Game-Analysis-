import re

def table(action):
  ThreeP = (re.compile(r'([\S]. [\S]*) makes 3-pt jump shot from').search(action), '3P')
  TwoP = (re.compile(r'([\S]. [\S]*) makes 2-pt jump shot from').search(action), 'FG')
  LayUp = (re.compile(r'([\S]. [\S]*) makes 2-pt layup').search(action), 'FG')
  Dunk = (re.compile(r'([\S]. [\S]*) makes 2-pt jump dunk').search(action), 'FG')
  ThreeP_missed = (re.compile(r'([\S]. [\S]*) misses 3-pt jump shot from').search(action), '3PA')
  TwoPJumpShot_missed = (re.compile(r'([\S]. [\S]*) misses 2-pt jump shot from').search(action), '3P')
  TwoPLayup_missed = (re.compile(r'([\S]. [\S]*) misses 2-pt layup').search(action), 'FGA')
  DRB = (re.compile(r'Defensive rebound by ([\S]+\. [\S]*)').search(action), 'DRB')
  ORB = (re.compile(r'Offensive rebound by ([\S]. [\S]*[^) ])').search(action), 'ORB')
  FT = (re.compile(r'([\S]. [\S]*) makes free thow (.*)').search(action), 'FT')
  FTClear = (re.compile(r'([\S]. [\S]*) makes clear path free throw (.*) of (.*)').search(action), 'FT')
  FTA = (re.compile(r'([\S]. [\S]*) misses free throw (.*) of (.*)').search(action), 'FGA')
  HookShot_missed = (re.compile(r'([\S]. [\S]*) misses 2-pt hook shot from').search(action), 'FGA')
  HookShot = (re.compile(r'([\S]. [\S]*) makes 2-pt hook shot from').search(action), 'FG')
  TOV = (re.compile(r'Turnover by ([\S]. [\S]*[^) ])').search(action), 'TOV')
  AST = (re.compile(r'assist by ([\S]. [\S]*[^)])').search(action), 'AST')
  STL = (re.compile(r'steal by ([\S]. [\S]*[^) ])').search(action), 'STL')
  BLK = (re.compile(r'block by ([\S]. [\S]*[^) ])').search(action), 'BLK')
  PF = (re.compile(r'Personal foul by ([\S]+\. [\S]*)').search(action), 'PF')
  SHF = (re.compile(r'Shooting foul by ([\S]+\. [\S]*[^) ])').search(action), 'PF')
  OF = (re.compile(r'Offensive foul by ([\S]. [\S]*[^) ])').search(action), 'PF')
  CF = (re.compile(r'Clear path foul by ([\S]. [\S]*[^) ])').search(action), 'PF')
  LBF = (re.compile(r'Loose ball foul by ([\S]. [\S]*[^) ])').search(action), 'PF')
  re_data = (ThreeP, TwoP, LayUp, Dunk, ThreeP_missed, TwoPJumpShot_missed, TwoPLayup_missed, DRB, ORB, FT,
             FTA, TOV, AST, STL, BLK, PF, SHF, OF, CF, LBF, HookShot_missed, HookShot, FTClear)
  return [r for r in re_data if r[0] is not None]