class Solution:
    def overlap(self, i1, i2):
        # returns true if i1 and i2 overlap, and false otherwise
        if i1[0] < i2[0]:
            # i1 comes first
            if i1[1] >= i2[0]:
                return True

        else:
            #i2 comes first
            if i2[1] >= i1[0]:
                return True

        return False
    def insert(self, intervals, newInterval):
                # 1) insert with no merge
        newLst = []
        app = False
        inserted = False
 
        for i in range(len(intervals)):
            if not inserted:
                # we pick the start to be the smaller of the two
                start = min(newInterval[0], intervals[i][0])
                print(f"starting with {start}")
                if self.overlap(newInterval, intervals[i]):
                    # if we have overlap, we take the end to be the bigger one... 
                    print("overlap!")
                    end = max(newInterval[1], intervals[i][1])
                    print(f"ending at {end} for now")
                    # but now we need to look even further... 
                    # if end == newInterval[1] I might need to keep looking further... 
                    if end == newInterval[1]:
                        print("need to look forward futher just to make sure...")
                        found_end = False
                        while i < len(intervals) - 1:
                            if found_end:
                                newLst.append(intervals[i])
                            elif self.overlap(intervals[i + 1], [start, end]):
                                print("there is overlap with the next element")
                                end = max(intervals[i + 1][1], end)
                                # there are more cases here
                            else:
                                # there was no further overlap
                                newLst.append([start, end])
                                #newLst.append(intervals[i])
                                found_end = True
                            i += 1
                        # are we ending with the fancy new one?
                        if not found_end:
                            newLst.append([start, end])
                        else:
                            newLst.append(intervals[i])
                        return newLst
                        # do we need to add the last one manually, or is it a part of the merge?
                else:
                    # there must not have been any overlap...
                    end = min(intervals[i][1], newInterval[1])

                    # do I need to now append interval[i]?
                    if start != intervals[i][0]:
                        app = True
                
                if start <= newInterval[0] and end >= newInterval[1]:
                    # we check if its the new interval, so we can set inserted to true
                    inserted = True

                newLst.append([start, end])

                if app:
                    newLst.append(intervals[i])
            else:
                newLst.append(intervals[i])

        if not inserted:
            newLst.append(newInterval)
        return newLst
        