class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l_logs, d_logs = [], []
        
        for log in logs:
            if log.split()[1].isdigit():
                d_logs.append(log)
            else:
                l_logs.append(log)
        
        l_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return l_logs + d_logs