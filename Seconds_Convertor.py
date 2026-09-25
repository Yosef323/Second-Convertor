#                   25/9/2026
#مشروع لتحويل عدد الثواني الي كم ساعه ودقيقه وباقي الثواني

total_seconds=input('Please type the number of sec: ')
int_total_seconds=int(total_seconds)
hours=int_total_seconds//(60*60)
minutes=(int_total_seconds%(60*60))//60
seconds=(int_total_seconds%(60*60))%60

print('This mean: '+str(hours)+' hours, '+
     str(minutes)+' minutes and '+str(seconds) +' seccond long' )