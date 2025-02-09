class NamingConventionFormatter:
    def camel_case(self, name):
        """Convert to Camel Case."""
        words = name.split()
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

    def pascal_case(self, name):
        """Convert to Pascal Case."""
        words = name.split()
        return ''.join(word.capitalize() for word in words)

    def snake_case(self, name):
        """Convert to Snake Case."""
        words = name.split()
        return '_'.join(word.lower() for word in words)

    def kebab_case(self, name):
        """Convert to Kebab Case."""
        words = name.split()
        return '-'.join(word.lower() for word in words)

    def upper_case(self, name):
        """Convert to Upper Case (Screaming Snake Case)."""
        words = name.split()
        return '_'.join(word.upper() for word in words)

    def hungarian_notation(self, name, prefix):
        """Convert to Hungarian Notation with a given prefix."""
        return f"{prefix}{name}"

    def flat_case(self, name):
        """Convert to Flat Case."""
        words = name.split()
        return ''.join(word.lower() for word in words)

    def contextual_naming(self, name, action):
        """Convert to Contextual Naming."""
        return f"{action}{name.capitalize()}"