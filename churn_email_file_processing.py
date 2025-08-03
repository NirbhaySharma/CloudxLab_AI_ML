def count_number_of_lines():
    fhand = open('/cxldata/datasets/project/mbox-short.txt')
    count = 0
    for line in fhand:
        line = line.rstrip() # Remove new line characters from right
        if line.startswith('Subject:'):
            count +=1
    fhand.close()
    return count


def find_email_sent_days():
    fhand = open('/cxldata/datasets/project/mbox-short.txt')
    days = {}
    for line in fhand:
        line = line.rstrip() # Remove new line characters from right
        if line.startswith('From '):
            day = (line.split()[2])
            days[day] = days.get(day,0) + 1
    fhand.close()
    return days


def count_message_from_email():
    fhand = open('/cxldata/datasets/project/mbox-short.txt')
    senders = {}
    for line in fhand:
        line = line.rstrip() # Remove new line characters from right
        if line.startswith('From '):
            sender = (line.split()[1])
            senders[sender] = senders.get(sender,0) + 1
    fhand.close()
    return senders


def count_message_from_domain():
    fhand = open('/cxldata/datasets/project/mbox-short.txt')
    domains = {}
    for line in fhand:
        line = line.rstrip() # Remove new line characters from right
        if line.startswith('From '):
            domain = ((line.split()[1]).split('@'))[1]
            domains[domain] = domains.get(domain,0) + 1
    fhand.close()
    return domains


def average_spam_confidence():
    fhand = open('/cxldata/datasets/project/mbox-short.txt')
    count = 0
    sum = 0
    for line in fhand:
        line = line.rstrip() # Remove new line characters from right
        if line.startswith('X-DSPAM-Confidence:'):
            sum += (float) (line.split(':')[1])
            count += 1
    fhand.close()
    count = sum/count
    return count


count_number_of_lines()
count_message_from_email()
average_spam_confidence()
count_message_from_domain()
find_email_sent_days()
