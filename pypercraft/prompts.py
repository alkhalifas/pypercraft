GENERATE_TITLE_PROMPT = """
                Generate an appropriate clever title for the paper concerning the following idea and topic:

                Idea: {idea}

                Topic: {topic}

                Return the result as a single string, and do not mention the fact that this is a title or a paper.
                """

GENERATE_INTRODUCTION_PROMPT = """
        Generate an appropriate introduction for the paper concerning the following idea and topic:

        Idea: {idea}

        Topic: {topic}

        Make sure the length of the introduction is appropriate for a paper that is {num_pages} pages long.

        Return the result as a single string, and do not mention the fact that this is a introduction or a paper.
        """

GENERATE_BODY_PROMPT = """
        Generate appropriate body paragraphs for the paper concerning the following idea and topic:

        Idea: {idea}

        Topic: {topic}

        Make sure the length of the body is appropriate for a paper that is {num_pages} pages long.

        Return the result as a single string, and do not mention the fact that this is a body or a paper.
        """

GENERATE_CONCLUSION_PROMPT = """
        Generate an appropriate conclusion for the paper concerning the following idea and topic:

        Idea: {idea}

        Topic: {topic}

        Make sure the length of the conclusion is appropriate for a paper that is {num_pages} pages long.

        Return the result as a single string, and do not mention the fact that this is a conclusion or a paper.
        """