class ObservesEvents:
    def observe_events(self, entity, event):
        if entity.__has_events__ == True:
            for observer in entity.__observers__.get(entity.__class__, []):
                try:
                    getattr(observer, event)(entity)
                except AttributeError:
                    pass

    @classmethod
    def observe(cls, observer):
        if cls in cls.__observers__:
            cls.__observers__[cls].append(observer)
        else:
            cls.__observers__.update({cls: [observer]})

    @classmethod
    def without_events(cls):
        """Sets __has_events__ attribute on entity to false."""
        cls.__has_events__ = False
        return cls

    @classmethod
    def with_events(cls):
        """Sets __has_events__ attribute on entity to True."""
        cls.__has_events__ = True
        return cls


class ObserveableTrait(ObservesEvents):
    __observers__ = {}
    __has_events__ = True


