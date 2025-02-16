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
    
    def format_frontend_container(self, module_name, function_name):
        """Format the module and function name as [ModuleName][Function]Page.tsx"""
        module = self.pascal_case(module_name)
        function = self.pascal_case(function_name)
        return f"{module}{function}Page.tsx"
    
    def format_frontend_component(self, module_name, function_name):
        """Format the module and function name as [ModuleName][Function].tsx"""
        module = self.pascal_case(module_name)
        function = self.pascal_case(function_name)

        return f"{module}{function}.tsx"

    def format_frontend_reducer(self, module_name, function_name):
        """Format as [module]-[function].ts"""
        return f"{module_name.lower()}-{function_name.lower()}.ts"

    def format_frontend_saga(self, module_name):
        """Format as [module].ts"""
        return f"{module_name.lower()}Saga.ts"

    def format_backend_rest_controller(self, module_name):
        """Format as [Module]RestController.java"""
        module = self.pascal_case(module_name)

        return f"{module}RestController.java"

    def format_backend_service(self, module_name):
        """Format as [Module]Service.java"""
        module = self.pascal_case(module_name)

        return f"{module}Service.java"
    
    def format_backend_service_implement(self, module_name):
        """Format as [Module]Service.java"""
        module = self.pascal_case(module_name)
        
        return f"{module}ServiceImpl.java"
    
    def format_error_message(self, module_name, error):
        """Format as ERR_[MODULE]_[ERROR]"""
        return f"ERR_{module_name}_{error}"