from django.db import models
from index_generator.models import Pool
from library_sample_shared.models import ReadLength


class Sequencer(models.Model):
    name = models.CharField('Name', max_length=50)
    lanes = models.PositiveSmallIntegerField('Number of Lanes')
    lane_capacity = models.PositiveSmallIntegerField('Lane Capacity')

    def __str__(self):
        return self.name


class Lane(models.Model):
    name = models.CharField('Name', max_length=5)
    pool = models.ForeignKey(Pool, related_name='pool', verbose_name='Pool')
    loading_concentration = models.FloatField('Loading Concentration')

    def __str__(self):
        return '%s: %s' % (self.name, self.pool.name)


class Flowcell(models.Model):
    flowcell_id = models.CharField('Flowcell ID', max_length=50)

    read_length = models.ForeignKey(
        ReadLength,
        related_name='read_length',
        verbose_name='Read Length',
    )

    lanes = models.ManyToManyField(Lane, blank=True)

    def __str__(self):
        return self.flowcell_id