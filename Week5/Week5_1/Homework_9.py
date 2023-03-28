"""Print the value of key 'history' from the below dict
sampleDict = {
    'class': {
        'student': {
            'name': 'Mike',
            'marks': {
                'physics': 70,
                'history': 80
            }
        }
    }
}"""



sampleDict = {
    'class': {
        'student': {
            'name': "Mike",
            'marks': {
                'physics': 70,
                'history': 80
            }
        }
    }
}

val = sampleDict['class']['student']['marks'].get('history')
print(val)