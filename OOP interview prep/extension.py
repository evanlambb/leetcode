from abc import ABC, abstractmethod
from typing import List
from enum import Enum



class Vote(Enum):
  ALLOW = 1
  ABSTAIN = 0
  BLOCK = -1

class ContentFilter(ABC):
  
  @abstractmethod
  def vote(self, title : str, channel : str) -> Vote: # takes in the Video title 
    pass


class ChannelOverride(ContentFilter):
  def vote(self, title : str, channel : str) -> Vote:  if channel == "MIT OpenCourseWare": 
    return Vote.ALLOW
  return Vote.ABSTAIN

class MLFilter(ContentFilter):
  def vote(self, title : str, channel : str) -> Vote:
    if "let's play" in title or "prank" in title:
      return Vote.BLOCK
    elif "tutorial" in title or "education" in title:
      return Vote.ALLOW
    return Vote.ABSTAIN

class VideoEvaluator:
  def __init__(self):
    self.filters = []
    # if 50% of the votes are BLOCK, then block the video, if 50% are accept then except else ABSTAIN
  def evaluate_video(self, title : str, channel : str) -> Vote:
    votes = [f.vote(title, channel) for f in self.filters]
    allow = votes.count(Vote.ALLOW)
    block = votes.count(Vote.BLOCK)
    abstain = votes.count(Vote.ABSTAIN)
    if block > allow and block > abstain:
      return Vote.BLOCK
    elif allow > block and allow > abstain:
      return Vote.ALLOW
    else:
      return Vote.ABSTAIN

  def attach(self, filter : ContentFilter):
    self.filters.append(filter)
