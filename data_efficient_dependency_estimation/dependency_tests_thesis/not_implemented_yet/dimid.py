import numpy
import tensorflow as tf

from active_learning_ts.knowledge_discovery.knowledge_discovery_task import KnowledgeDiscoveryTask
from active_learning_ts.query_selection.query_sampler import QuerySampler
from active_learning_ts.queryable import Queryable


class DIMID(KnowledgeDiscoveryTask):

    def __init__(self) -> None:
        super().__init__()
        self.global_uncertainty = 0

    def dimid(x,y):
        return 0

    def updateDIMID():
        return 0

    def initDIMID():
        return 0

    def learn(self, num_queries):
        """
        Following the pseudo code
        """
        self.sampler.update_pool(self.surrogate_model.get_query_pool())
        query = self.sampler.sample(num_queries)
        xs, ys = self.surrogate_model.query(query)
        
        r, p = self.dimid(xs,ys)
        self.global_uncertainty = p

        return r, p


    def uncertainty(self, points: tf.Tensor) -> tf.Tensor:
        return tf.fill(points.shape, self.global_uncertainty)