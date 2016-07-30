import random
import luigi


class FirstStep(luigi.Task):
    max_value = luigi.IntParameter()
    def requires(self):
        return []
    def output(self):
        return luigi.LocalTarget('outputs/number_less_than_{}.txt'.format(self.max_value))
    def run(self):
        with self.output().open('w') as out_file:
            output = int(round(random.random() * self.max_value))
            out_file.write('{}'.format(output))

class SecondStep(luigi.Task):
    def requires(self):
        return [FirstStep(max_value=5)]
    def output(self):
        return luigi.LocalTarget('outputs/random_number_squared.txt')
    def run(self):
        with self.output().open('w') as out_file, self.input()[0].open() as in_file:
            value = int(in_file.read())
            out_file.write(str(value*value))

if __name__ == '__main__':
    luigi.run()

