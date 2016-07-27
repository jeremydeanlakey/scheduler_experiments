""" somewhat following the tutorial at http://help.mortardata.com/technologies/luigi/how_luigi_works """

import luigi


class MyTarget(luigi.Target):
    def exists(self):
        return True


class MyExampleTask(luigi.Task):
    # Example parameter for our task: a 
    # date for which a report should be run
    report_date = luigi.DateParameter()
    
    def requires(self):
        return [MyTarget()]
    
    def output(self):
        return luigi.LocalTarget("test.txt")
    
    def run(self):
        open('test.txt', 'w').write('blah')

# luigi --module test_luigi MyExampleTask --local-scheduler

