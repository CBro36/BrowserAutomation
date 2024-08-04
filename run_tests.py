import unittest

loader = unittest.TestLoader()
testDir = 'Tests'
suite = loader.discover(testDir)

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

runRate = (result.testsRun - len(result.errors)) / result.testsRun
passRate = (result.testsRun - (len(result.errors) + len(result.failures))) / result.testsRun

print('-----Exit Criteria-----')
print(f'\nRun Rate: {runRate:.2f}')
print(f'Pass Rate: {passRate:.2f}')

if runRate < 0.98 or passRate < 0.9:
    print('\nExit Criteria Failed')
else:
    print('\nExit Criteria Passed')